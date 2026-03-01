from fastapi import APIRouter, Response, HTTPException, Depends
from database import supabase
from models import HoneyCreate, HoneyUpdate
from auth import get_current_user

router = APIRouter(
    prefix="/honey",
    tags = ["honeys"]
)

@router.get('/')
def get_all_honeys():
    content = supabase.table("honeys").select("*").execute()
    return content.data

@router.get('/{id}')
def get_honey(id: int):
    content = supabase.table("honeys").select("*").match({"id":id}).execute()
    if not content.data:
        raise HTTPException(
            status_code=404,
            detail="Honey record not found."
        )
    return content.data[0] # default return type of content.data is a list, this ensures we are getting the 1st entry

@router.post("/", status_code=201)
def create_honey(honey: HoneyCreate, current_user: str = Depends(get_current_user)):
    # call external api to update longitude and latitude coordinates
    content = supabase.table("honeys").insert(honey.model_dump()).execute()
    return content.data

@router.delete('/{id}')
def delete_honey(id: int, current_user: str = Depends(get_current_user)):
    content = supabase.table("honeys").delete().eq("id", id).execute()
    if not content.data:
        raise HTTPException(
            status_code=404,
            detail="Honey record not found."
        )
    return Response(status_code=204)

@router.put('/{id}')
def update_honey(id: int, honey: HoneyUpdate, current_user: str = Depends(get_current_user)):
    content = supabase.table("honeys").update(honey.model_dump(exclude_none=True)).eq("id", id).execute()
    if not content.data:
        raise HTTPException(
            status_code=404,
            detail="Honey record not found."
        )
    return content.data