import graphene
import app.schema
#from django.contrib.
#from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView
# import users.schema

#class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
#    pass

class Mutation(app.schema.Mutation,graphene.ObjectType):
    pass

class Query(app.schema.Query,graphene.ObjectType):
    pass
# class Subscription(app.schema.Subscription,graphene.ObjectType):
#     pass 

schema = graphene.Schema(query=Query,mutation=Mutation)