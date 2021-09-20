import { combineReducers } from 'redux'
import userReducer from './user';

export default combineReducers({
    // products:productsReducer,
    // bills:billReducer,
    user:userReducer,
    // login:loginReducer,
    // category:categoryReducer,
    // width:widthReducer,
    // bankTab:bankTabReducer,
})
