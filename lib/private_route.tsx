// import { NextPageContext } from "next";
import React, { Component } from "react";
import { AuthToken } from "./auth_token";
import ServerCookie from "next-cookies";
// import {getCurrentUser} from './authentication'

// import { redirectToLogin } from "./redirectService";

export type AuthProps = {
    auth: AuthToken
  }
  
  export function privateRoute(WrappedComponent: any) {
    return class extends Component<AuthProps> {
      static async getInitialProps(ctx: any) {
        // console.log(ctx)
        
        const token = ServerCookie(ctx)["token"];
        console.log(WrappedComponent)
        // const token = localStorage.getItem("token")
        console.log("below is token")
        
        // console.log(token)
        const auth = new AuthToken(token);
        const initialProps = { auth };
        // console.log(auth)
        if (auth.isExpired || auth.token==undefined) {
          ctx.res.writeHead(302, {
            Location: "/login?redirected=true",
          });
          ctx.res.end();
        }
        if (WrappedComponent.getInitialProps) return WrappedComponent.getInitialProps(initialProps);
        return initialProps;
      }
  
      get auth() {
        // the server pass to the client serializes the token
        // so we have to reinitialize the authToken class
        //
        // @see https://github.com/zeit/next.js/issues/3536
        return new AuthToken(this.props.auth.token);
      }
      // get user async(){
      //   return await getCurrentUser().then((e)=>e);
      // }

      
  
      render() {
        return <WrappedComponent auth={this.auth}  {...this.props} />;
      }
    };
  }