from fastapi import Header
from fastapi import HTTPException

from app.auth.simulated_roles import ROLES


def require_role(
    permission: str
):

    async def checker(
        x_role: str = Header(...)
    ):

        role = x_role.lower()

        if role not in ROLES:

            raise HTTPException(
                status_code=403,
                detail="Invalid role"
            )

        if permission not in ROLES[role]:

            raise HTTPException(
                status_code=403,
                detail="Permission denied"
            )

        return role

    return checker