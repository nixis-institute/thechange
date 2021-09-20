# from typing_extensions import Required
import graphene
from app.models import *
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from graphene import relay
from django.contrib.auth.models import User
from graphene.relay.node import from_global_id
from django.contrib.auth import get_user_model
import graphql_jwt


class SocietyNode(DjangoObjectType):
    class Meta:
        model = Society
        filter_fields=()
        interfaces = (relay.Node,)

class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields=()
        interfaces = (relay.Node,)

class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields=()
        interfaces = (relay.Node,)

class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields=()
        interfaces = (relay.Node,)

class ShopNode(DjangoObjectType):
    class Meta:
        model = Shop
        filter_fields=()
        interfaces = (relay.Node,)

class ProfileNode(DjangoObjectType):
    class Meta:
        model = Profile
        filter_fields=()
        interfaces = (relay.Node,)

class CreateSociety(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        sector = graphene.String(required=True)
        address = graphene.String(required=True)
        city = graphene.String(required=True)
        state = graphene.String(required=True)
        pincode = graphene.String(required=True)
    success = graphene.Boolean()
    society = graphene.Field(SocietyNode)
    def mutate(self,info,name,sector,address,city,state,pincode):
        s = Society.objects.create(name = name,sector = sector,address = address,city = city, state = state, pincode  = pincode
        )
        return CreateSociety(success=True,society = s)

class UpdateSociety(graphene.Mutation):
    class Arguments:
        is_delete = graphene.Boolean(required=True)
        id = graphene.ID(required=True)
        name = graphene.String(required=False)
        sector = graphene.String(required=False)
        address = graphene.String(required=False)
        city = graphene.String(required=False)
        state = graphene.String(required=False)
        pincode = graphene.String(required=False)
    success = graphene.Boolean()
    # society = graphene.Field(SocietyNode)
    def mutate(self,info,id,name,sector,address,city,state,pincode,is_delete):
        society = Society.objects.get(id = from_global_id(id)[1])
        if(is_delete):
            society.delete()
        else:
            society.name = name
            society.sector = sector
            society.address = address
            society.city = city 
            society.state = state 
            society.pincode  = pincode
            society.save()
        
        return UpdateSociety(success=True)
    
class CreateProduct(graphene.Mutation):
    class Arguments:
        society_id = graphene.ID(required=True)
        name = graphene.String(required=True)
        price = graphene.Float(required=True)
        description = graphene.String(required=True)
        purchase_year = graphene.Int(required=False)
        model = graphene.String(required=False)
        is_negotiable = graphene.Boolean(required=True)
        
    success = graphene.Boolean()
    product = graphene.Field(ProductNode)
    def mutate(self,info,society_id,name,price,description,purchase_year,model,is_negotiable):
        s = Product.objects.create(
            user_id = 1,
            society_id = from_global_id(society_id)[1],
            name = name,
            price = price,
            description = description,
            purchase_year = purchase_year,
            model = model,
            is_negotiable = is_negotiable
        )
        return CreateProduct(success=True,product = s)

class UpdateProduct(graphene.Mutation):
    class Arguments:
        is_delete = graphene.Boolean(required=True)
        product_id = graphene.ID(required=True)
        society_id = graphene.ID(required=True)
        name = graphene.String(required=False)
        price = graphene.Float(required=False)
        description = graphene.String(required=False)
        purchase_year = graphene.Int(required=False)
        model = graphene.String(required=False)
        is_negotiable = graphene.Boolean(required=False)
    success = graphene.Boolean()
    def mutate(self,info,is_delete,product_id,society_id,name,price,description,purchase_year,model,is_negotiable):
        product = Product.objects.get(id = from_global_id(product_id)[1])
        if(is_delete):
            product.delete()
        else:
                product.user_id = 1,
                product.society_id = from_global_id(society_id)[1],
                product.name = name,
                product.price = price,
                product.description = description,
                product.purchase_year = purchase_year,
                product.model = model,
                product.is_negotiable = is_negotiable
                product.save()
            
        return UpdateProduct(success=True)

class CreateShop(graphene.Mutation):
    class Arguments:
        society_id = graphene.ID(required=True)
        name = graphene.String(required=True)
        number = graphene.String(required=True)
        s_type = graphene.String(required=True)
        contact = graphene.String(required=True)
        email = graphene.String(required=False)
        items = graphene.String(required=False)
        # is_negotiable = graphene.Boolean(required=True)
        
    success = graphene.Boolean()
    shop = graphene.Field(ShopNode)
    def mutate(self,info,society_id,name,number,s_type,contact,email,items):
        s = Shop.objects.create(
            society_id = from_global_id(society_id)[1],
            user_id = 1,
            number = number,
            name = name,
            s_type = s_type,
            contact_number = contact,
            email = email,
            items = items
        )
        return CreateShop(success=True,shop = s)

class UpdateShop(graphene.Mutation):
    class Arguments:
        shop_id = graphene.ID(required=True)
        is_delete = graphene.Boolean(required=True)
        society_id = graphene.ID(required=False)
        name = graphene.String(required=False)
        number = graphene.String(required=False)
        s_type = graphene.String(required=False)
        contact = graphene.String(required=False)
        email = graphene.String(required=False)
        items = graphene.String(required=False)
        
    success = graphene.Boolean()
    # shop = graphene.Field(ShopNode)
    def mutate(self,info,shop_id,is_delete,society_id,name,number,s_type,contact,email,items):
        shop = Shop.objects.get(id = from_global_id(shop_id)[1])
        if(is_delete):
            shop.delete()
        else:
            shop.society_id = from_global_id(society_id)[1]
            shop.user_id = 1
            shop.number = number
            shop.name = name
            shop.s_type = s_type
            shop.contact_number = contact
            shop.email = email
            shop.items = items
            shop.save()

        return UpdateShop(success=True)

class CreateCategory(graphene.Mutation):
    class Arguments:
        shop_id = graphene.ID(required=True)
        name = graphene.String(required=True)
        
    success = graphene.Boolean()
    category = graphene.Field(CategoryNode)
    def mutate(self,info,shop_id,name):
        s = Category.objects.create(
            shop_id = from_global_id(shop_id)[1],
            name = name,
        )
        return CreateCategory(success=True,category = s)

class UpdateCategory(graphene.Mutation):
    class Arguments:
        is_delete = graphene.Boolean(required=True)
        shop_id = graphene.ID(required=True)
        category_id = graphene.ID(required=True)
        name = graphene.String(required=True)
        
    success = graphene.Boolean()
    def mutate(self,info,shop_id,name,category_id,is_delete):
        category = Category.objects.get(id = from_global_id(category_id)[1])
        if(is_delete):
            category.delete()
        else:
            category.shop_id = from_global_id(shop_id)[1]
            category.name = name
            category.save()
            
        return UpdateCategory(success=True)

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        firstname = graphene.String(required=True)
        lastname = graphene.String(required=True)
        phone = graphene.String(required=True)

        society_id = graphene.ID(required = True)
        alternative_phone = graphene.String(required=True)
        tower_number = graphene.String(required=True)
        flat_no = graphene.String(required = True)

    user = graphene.Field(UserNode)
    success = graphene.Boolean()

    def mutate(self,info,username,password,email,firstname,lastname,phone,society_id,alternative_phone,tower_number,flat_no):
        user = get_user_model()(username = username,email = email,first_name = firstname,last_name=lastname)
        user.set_password(password)
        user.save()
        Profile.objects.create(
            user_id = user.id,
            society_id = from_global_id(society_id)[1],
            phone = phone,
            alternative_phone = alternative_phone,
            tower_number = tower_number,
            flat_no = flat_no
            )
        return CreateUser(user=user,success = True)

class UpdateUser(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        firstname = graphene.String(required=True)
        lastname = graphene.String(required=True)
        phone = graphene.String(required=True)

        society_id = graphene.ID(required = True)
        alternative_phone = graphene.String(required=True)
        tower_number = graphene.String(required=True)
        flat_no = graphene.String(required = True)

    success = graphene.Boolean()
    def mutate(self,info,user_id,username,email,firstname,lastname,phone,society_id,alternative_phone,tower_number,flat_no):
        user = User.objects.get(id = from_global_id(user_id)[1])
        user.username = username
        user.email = email
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        
        s = Profile.objects.get(user_id = user.id)
        s.society_id = from_global_id(society_id)[1]
        s.phone = phone
        s.alternative_phone = alternative_phone
        s.tower_number = tower_number
        s.flat_no = flat_no
        s.save()
        
        return UpdateUser(success = True)


class Mutation(graphene.ObjectType):
    # token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    create_society = CreateSociety.Field()
    create_product = CreateProduct.Field()
    create_shop = CreateShop.Field()
    create_category = CreateCategory.Field()
    create_user = CreateUser.Field()
    update_society = UpdateSociety.Field()
    update_product = UpdateProduct.Field()
    update_shop = UpdateShop.Field()
    update_category = UpdateCategory.Field()
    update_user = UpdateUser.Field()

class Query(graphene.AbstractType):
    socity = graphene.Field(SocietyNode,id=graphene.ID())
    societies = DjangoFilterConnectionField(SocietyNode,search=graphene.String())
    users = DjangoFilterConnectionField(UserNode,search=graphene.String())
    products = DjangoFilterConnectionField(ProductNode,search=graphene.String())
    product = graphene.Field(ProductNode,id=graphene.ID())
    categories = DjangoFilterConnectionField(CategoryNode,search=graphene.String())
    category = graphene.Field(CategoryNode,id=graphene.ID())
    shops = DjangoFilterConnectionField(ShopNode,search=graphene.String())
    shop = graphene.Field(CategoryNode,id=graphene.ID())
    profiles = DjangoFilterConnectionField(ProfileNode,search=graphene.String())
    
    def resolve_socity(self,info,id):
        return Society.objects.get(id=from_global_id(id)[1])
    def resolve_product(self,info,id):
        return Product.objects.get(id=from_global_id(id)[1])
    def resolve_category(self,info,id):
        return Category.objects.get(id=from_global_id(id)[1])
    def resolve_shop(self,info,id):
        return Shop.objects.get(id=from_global_id(id)[1])                        

    def resolve_users(self,info):
        print(info.context.user)
        return User.objects.all()

    def resolve_societies(self,info):
        return Society.objects.all()

    def resolve_products(self,info):
        return Product.objects.all()

    def resolve_categories(self,info):
        return Category.objects.all()

    def resolve_shops(self,info):
        return Shop.objects.all()

    def resolve_profiles(self,info):
        return Profile.objects.all()


# schema = graphene.Schema(query=Query)