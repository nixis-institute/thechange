
import {useForm} from 'react-hook-form'
import { useMutation, useQuery } from '@apollo/client';
import {GetToken} from '../lib/Graphql'
import {AuthToken} from '../lib/auth_token'
import Layout from '../components/Layout';

import { ApolloProvider } from '@apollo/client'
import client from '../lib/apolloClient'

// import { useEffect } from 'react';


const Login = ()=>{
    const { register, handleSubmit, watch, errors } = useForm();
    const [_getToken,{data:tokenData,loading:tokenloading}] = useMutation(GetToken)

    const OnSubmit=(data)=>{

        console.log(data)
        _getToken({
            variables:{
                'username':data.username,
                'password':data.password
            }
        }).then(e=>{
            console.log(e.data.tokenAuth.token)
            AuthToken.storeToken(e.data.tokenAuth.token)
        }).catch(e=>{
            console.log(e)
        })
    }



    return(
        
        <Layout title = {"Login"}>
            {/* <h1>Login</h1> */}
                <div>
                    <h1>Welcome Back</h1>
                    <div className="login_form">
                        <form onSubmit={handleSubmit(OnSubmit)}>
                            <div style={{ width:"40%",margin:"0 auto"}}>
                                <div className="columns">
                                    <div className="column">
                                        <label className="label">Username</label>
                                        <input type="text" className="input is-rounded" name="username" {...register('username', { required: true })} autoComplete="off" placeholder="Username"/>
                                    </div>
                                </div>

                                <div className="columns">
                                    <div className="column">
                                        <label className="label">Password</label>
                                        <input type="password" className="input is-rounded" name="password" {...register('password', { required: true })} autoComplete="off" placeholder="Password"/>
                                    </div>
                                </div>

                                <div className="columns">
                                    <div className="column">
                                        <input type="submit" className="button is-primary is-rounded" name="submit" autoComplete="off" value="Login"/>
                                    </div>
                                </div>                                
                            </div>
                        </form>
                    </div>
                </div> 
        </Layout>
        
        
    )
}



// const X = () =>{
//     return <Layout title = {"Welcome to Login"}>
//                 <Login/>
//         </Layout>
// }


export default Login