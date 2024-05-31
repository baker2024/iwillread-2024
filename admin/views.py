from sqladmin import ModelView

from products.models import Product, Category
from users.models import User


class UsersAdmin(ModelView, model=User):
    column_list = [User.id, User.surname, User.name, User.patronymic, User.login, User.email, User.phone]
    column_details_exclude_list = [User.hashed_password]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"


class ProductsAdmin(ModelView, model=Product):
    column_list = [Product.category, Product.name, Product.description, Product.price, Product.count, Product.image_id]
    column_labels = {
        Product.id: "ID",
        Product.category_id: "ID Категории",
        Product.name: "Название",
        Product.description: "Описание",
        Product.price: "Цена"
    }

    name = "Товар"
    name_plural = "Товары"
    icon = "fa-brands fa-product-hunt"


class CategoriesAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.name]
    column_labels = {
        Category.id: "ID",
        Category.name: "Название",
    }
    name = "Категория"
    name_plural = "Категории"
    icon = "fa-solid fa-list"
