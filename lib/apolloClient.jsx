import {ApolloClient,InMemoryCache,ApolloLink} from '@apollo/client'
import {createHttpLink} from 'apollo-link-http'
import Cookie from 'js-cookie'

const _server = "http://localhost:8000/graphql"

  // const authLink = setContext((_, { headers }) => {
  //   const token = Cookie.get("token") 
  //   // const token = localStorage.getItem("token")

  //   // console.log("this.is token fro cookie")
  //   // console.log(token)
  //   if(token=="undefined"){
  //     token = ""
  //   }


  //   return {
  //     headers:{
  //       ...headers,
  //       'Authorization':`JWT ${token==undefined?"":token}`
  //     }
  //   }
  // });  


  const authLink = new ApolloLink((operation, forward) => {
    const token = Cookie.get("token")
    if(token=="undefined"){
      token = ""
    }    
    operation.setContext(({ headers }) => ({ headers: {

      // authorization: Auth.userId(), // however you get your token
      authorization:`JWT ${token==undefined?"":token}`,
      ...headers
    }}));
    return forward(operation);
  });


  const httplink = createHttpLink({
    uri:_server,
    credentials: 'same-origin'
    // credentials: 'include'
  });

  const client = new ApolloClient({
    // uri: _server,
    link:authLink.concat(httplink),
    cache: new InMemoryCache()
  });


// const httplink = createHttpLink({
//     uri:_server,
//     credentials: 'same-origin'
//   });




//   const authLink = setContext((_, { headers }) => {
//     const token = Cookie.get("token") 
//     if(token=="undefined"){
//       token = ""
//     }


//     return {
//       headers:{
//         ...headers,
//         ...(token ? {authorization: `JWT ${token}`} : {}),
//         // 'Authorization':`JWT ${token==undefined?"":token}`
//       },
//       ...context,
//     }
//   });


// const client = new ApolloClient({
//     link: authLink.concat(httplink),
//     cache : new InMemoryCache(),
// })


export default client
