import { DEBUG, SRC_DIR } from '../../../consts'
import { reImage, reStyle, staticAssetName } from '../consts'


// ...
export default {
    test: reImage,
    rules: [{
        test: /\.svg$/,
        loader: 'svg-url-loader',
        options: {
            name: staticAssetName,
            limit: 4096, // 4kb
        },           
    },{
        test: /favicon\.png$/,    
        loader: 'file-loader',
        options: {
            name: '[name].[ext]'
            // name: '[hash:8].[ext]'            
            // limit: 4096, // 4kb
        }, 
    },{
        test: /(?<!favicon)\.(jpg|png)$/,
        // include: /\/src\/resources\//,
        loader: 'file-loader',
        options: {
            name: '[1]',
            regExp: /src\/(.+)/,
            // name (fullname){
            //     return /src\/(.+)/.exec(fullname)[1]
            // }
        }, 
    }] 
}

