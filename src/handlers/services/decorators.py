from utils.database import Session, User


def inject_user_and_session(handler):
    async def function(message, state):
        with Session() as session:
            user = session.query(User).filter_by(chat_id=str(message.from_user.id)).first()
            return await handler(message, session, user, state)
    return function
