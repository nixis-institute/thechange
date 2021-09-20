import Layout from "./Layout"
import { useMutation, useQuery } from '@apollo/client';
import { _getSoceity } from "../lib/Graphql";


const S = () =>{
    const {data:soceites,loading:pageLoading} = useQuery(_getSoceity)
    
    return <>
    {pageLoading == true?<h1>Loading...</h1>:
    
    <div>
        {
            soceites.societies.edges.map((item,i)=>{
                return <>
                    <div key={i} >
                        <h2>{item.node.name}</h2>
                        <div>{item.node.address}</div>
                        <div>{item.node.state}</div>
                        <div>{item.node.city}</div>
                        <div>{item.node.pincode}</div>
                    </div>
                </>
            })
        }
    </div>
    
    }

    </>
}




const Soceity = () =>{
    return <>
        <Layout title = "Find Soceity">
            <S/>
        </Layout>
    </>
}

export default Soceity