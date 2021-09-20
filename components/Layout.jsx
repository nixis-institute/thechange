import Head from 'next/head'
import { ApolloProvider } from '@apollo/client'
import client from '../lib/apolloClient'
import React from 'react'


class Layout extends React.Component{
    constructor(props) {
        super(props);
    }
    static async getInitialProps({ req }) {
        let pageProps = {};
        if (Component.getInitialProps) {
            pageProps = await Component.getInitialProps(ctx);
        }
    
        return { pageProps };
        }
    render(){

        // let route = this.props.router.pathname;
        console.log(this.props)
        const { children,active,loading,loadingText,title = "The Change",sidebar=true,navbar=true,text,setText,login,side_bar,body_color } = this.props;
        
        return(
            <ApolloProvider client={client}>
                <div>
                    <Head>
                        <title>{title}</title>
                        <meta charSet="utf-8" />
                        <meta name="viewport" content="initial-scale=1.0, width=device-width"/>
                    </Head>
                    <main className="main">
                        {children}
                    </main>
                </div>
            </ApolloProvider>
        )
    }
}


export default Layout