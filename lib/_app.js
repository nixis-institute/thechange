
import { ApolloProvider } from '@apollo/client'
import client from '../lib/apolloClient'
import NProgress from 'nprogress'
import 'nprogress/nprogress.css';
import 'bulma/css/bulma.css';
import Router from 'next/router'
// import 'nprogress/nprogress.css';

NProgress.configure({showSpinner:false,minimum:0.3})
// NProgress.set(0.4);

Router.events.on('routeChangeStart', () => NProgress.start()); 
// NProgress.set(0.4)
Router.events.on('routeChangeComplete', () => NProgress.done()); 
Router.events.on('routeChangeError', () => NProgress.done());



function MyApp({ Component, pageProps }) {
    return (
      <ApolloProvider client={client}>
        <Component {...pageProps} />
      </ApolloProvider>
    );
  }

  export default MyApp