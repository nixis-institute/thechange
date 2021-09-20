import jwtDecode from "jwt-decode";
import Cookie from "js-cookie";
// import client from './apolloClient';
import Router from "next/router"
// import { currentUserQuery} from './graphql'
export type DecodedToken = {
    readonly email: string;
    readonly exp: number;
  }
  
  export class AuthToken {
    readonly decodedToken: DecodedToken;
  
    constructor(readonly token?: string) {
      // we are going to default to an expired decodedToken
      this.decodedToken = { email: "", exp: 0 };
  
      // then try and decode the jwt using jwt-decode
      try {
        if (token) this.decodedToken = jwtDecode(token);
      } catch (e) {
      }
    }
  
    get authorizationString() {
      return `Bearer ${this.token}`;
    }
  
    get expiresAt(): Date {
      return new Date(this.decodedToken.exp * 1000);
    }
  
    get isExpired(): boolean {
      // return false
      // console.log("--------");
      // console.log(this.token);
      return this.token!="undefined"?false:true
      // console.log(new Date() > this.expiresAt);
      // return new Date() > this.expiresAt;
    }
  
    get isValid(): boolean {
      return !this.isExpired;
    }

    get isActive():boolean{
      if(this.token){
        return true
      }
      else return false
    }


    // get currentUser() : any{
      
    // } 

    static async storeToken(token: string) {
        Cookie.set("token", token);
        localStorage.setItem("token",token)
        // var res = await client.query({
        //   query:currentUserQuery
        // })

        await Router.push("/");
      }

    // fromNext(s): String {
    //     return "X"

    // }
  }
  