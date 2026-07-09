from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.core.dependencies import get_current_user

from app.models.user import User

from app.schemas.product import (
    ProductCreate,
    ProductResponse,
)

from app.schemas.import_product import (
    ImportProductRequest,
)

from app.schemas.recommendation import (
    RecommendationResponse,
)

from app.services.product_service import (
    create_product,
    get_products,
    get_product,
    delete_product,
)

from app.services.import_service import (
    import_product,
)

from app.services.recommendation_service import (
    analyze_product,
)

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


# ---------------------------------------------------
# Create Product
# ---------------------------------------------------

@router.post(
    "",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_product(
        db=db,
        user_id=current_user.id,
        product_data=product,
    )


# ---------------------------------------------------
# List Products
# ---------------------------------------------------

@router.get(
    "",
    response_model=list[ProductResponse],
)
def list_products(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_products(
        db=db,
        user_id=current_user.id,
    )


# ---------------------------------------------------
# Get Single Product
# ---------------------------------------------------

@router.get(
    "/{product_id}",
    response_model=ProductResponse,
)
def get_single_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    product = get_product(
        db=db,
        product_id=product_id,
        user_id=current_user.id,
    )

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    return product


# ---------------------------------------------------
# Delete Product
# ---------------------------------------------------

@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def remove_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    product = get_product(
        db=db,
        product_id=product_id,
        user_id=current_user.id,
    )

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    delete_product(
        db=db,
        product=product,
    )

    return


# ---------------------------------------------------
# Import Product
# ---------------------------------------------------

@router.post(
    "/import",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def import_product_endpoint(
    payload: ImportProductRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        product = import_product(
            db=db,
            url=str(payload.url),
            current_user=current_user,
        )

        return product

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Import failed: {str(e)}",
        )


# ---------------------------------------------------
# Recommendation Engine
# ---------------------------------------------------

@router.get(
    "/{product_id}/recommendation",
    response_model=RecommendationResponse,
)
def get_product_recommendation(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    product = get_product(
        db=db,
        product_id=product_id,
        user_id=current_user.id,
    )

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    recommendation = analyze_product(
        db=db,
        product_id=product_id,
    )

    if recommendation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recommendation not found",
        )

    return recommendation