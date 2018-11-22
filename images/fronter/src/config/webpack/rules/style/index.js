import 
    MiniCssExtractPlugin from 'mini-css-extract-plugin'
import 
    autoprefixer from 'autoprefixer'    
import { 
    DEBUG, 
    SRC_DIR } from '../../../consts'
import { 
    reStyle, 
    minimizeCssOptions, 
    localIdentName,
    browsersList } from '../consts'



// ...
export default {
    test: reStyle,
    rules: [{
        loader: MiniCssExtractPlugin.loader,
    },{
        loader: 'css-loader',
        options: {
            /*
            * https://github.com/webpack-contrib/css-loader#importloaders
            * 0 => no loaders (default); 
            * 1 => postcss-loader; 
            * 2 => postcss-loader, sass-loader
            */
            // importLoaders: 2,
            // ..
            sourceMap: DEBUG,
            minimize: DEBUG 
                ? false 
                : minimizeCssOptions,
        },
    },{
        loader: 'postcss-loader',
        options: {
            plugins: [
                autoprefixer({
                    browsers: browsersList,
                    flexbox: 'no-2009',                        
                })
            ]
        },
    // },{
    //     test: /\.scss$/,        
    //     loader:'resolve-url-loader',
    },{
        test: /\.scss$/,
        loader: 'sass-loader',
        options:{
            sourceMap:true,
        }
    }],
}