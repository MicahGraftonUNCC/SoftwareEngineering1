from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .models import models, schemas
from .controllers import orders, sandwiches, recipes, resources, order_details
from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


##endpoints for Orders table##
@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create_order(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.get_orders(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.get_one_orders(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.get_one_orders(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.get_one_orders(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)


##endpoints for Sandwich table##
@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches.create_sandwich(db=db, sandwich=sandwich)


@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["Sandwiches"])
def read_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.get_sandwiches(db)


@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.get_one_sandwich(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwich


@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def update_one_sandwich(sandwich_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    sandwich_db = sandwiches.get_one_sandwich(db, sandwich_id=sandwich_id)
    if sandwich_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwiches.update(db=db, sandwich=sandwich, sandwich_id=sandwich_id)


@app.delete("/sandwiches/{sandwich_id}", tags=["Sandwiches"])
def delete_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.get_one_sandwich(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwiches.delete(db=db, sandwich_id=sandwich_id)


##endpoints for recipe table##
@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create_recipe(db=db, recipe=recipe)


@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return recipes.get_recipes(db)


@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.get_one_recipe(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe


@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def update_one_recipe(recipe_id: int, recipe: schemas.Recipe, db: Session = Depends(get_db)):
    recipe_db = recipes.get_one_recipe(db, recipe_id=recipe_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipes.update(db=db, recipe=recipe, recipe_id=recipe_id)


@app.delete("/recipes/{recipe_id}", tags=["Recipes"])
def delete_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.get_one_recipe(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe.delete(db=db, recipe_id=recipe_id)

##endpoints for resource table##
@app.post("/resources/", response_model=schemas.Resource, tags=["Resources"])
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create_resource(db=db, resource=resource)


@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resources"])
def read_resources(db: Session = Depends(get_db)):
    return resources.get_resources(db)


@app.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.get_one_resource(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource


@app.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def update_one_resource(resource_id: int, resource: schemas.Resource, db: Session = Depends(get_db)):
    resource_db = resources.get_one_resource(db, resource_id=resource_id)
    if resource_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resources.update(db=db, resource=resource, resource_id=resource_id)


@app.delete("/resources/{resource_id}", tags=["Resources"])
def delete_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.get_one_resource(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource.delete(db=db, resource_id=resource_id)

##endpoints for order_details table##
@app.post("/order_details/", response_model=schemas.OrderDetail, tags=["Order_Details"])
def create_order_detail(order_detail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details.create_order_detail(db=db, order_detail=order_detail)


@app.get("/order_details/", response_model=list[schemas.OrderDetail], tags=["Order_Details"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details.get_order_details(db)


@app.get("/order_details/{order_detail_id}", response_model=schemas.OrderDetail, tags=["Order_Details"])
def read_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    order_detail = order_details.get_one_order_detail(db, order_detail_id=order_detail_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_detail


@app.put("/order_details/{order_detail_id}", response_model=schemas.OrderDetail, tags=["Order_Details"])
def update_one_order_detail(order_detail_id: int, order_detail: schemas.OrderDetail, db: Session = Depends(get_db)):
    order_detail_db = order_details.get_one_order_detail(db, order_detail_id=order_detail_id)
    if order_detail_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_details.update(db=db, order_detail=order_detail, order_detail_id=order_detail_id)


@app.delete("/order_details/{order_detail_id}", tags=["Order_Details"])
def delete_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    order_detail = order_details.get_one_order_detail(db, order_detail_id=order_detail_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_detail.delete(db=db, order_detail_id=order_detail_id)
