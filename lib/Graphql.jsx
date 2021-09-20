import gql from 'graphql-tag';



export const GetToken = gql`mutation getToken($username:String!,$password:String!){
	tokenAuth(username:$username,password:$password){
    token
  }
}`

export const _getSoceity = gql`query x{
  societies{
    edges{
      node{
        name
        sector
        address
        city
        state
        pincode
        verified
      }
    }
  }
}`