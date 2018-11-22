import 
    webpack from 'webpack'
import 
    webpackDevMiddleware from 'webpack-dev-middleware'
import 
    proxyMiddleware from 'http-proxy-middleware'

// ...
import 
    wpConfig, { 
    mwConfig as wpMwConfig
} from '../webpack'

// ...
import { 
    BROWSERSYNC_TARGET,
    BROWSERSYNC_PORT,
    BROWSERSYNC_HOST } from '../consts'

// .. WEBPACK
// =====================
const bundler = webpack(wpConfig)
const webpackMw = webpackDevMiddleware(bundler, wpMwConfig)


// PROXY
// =================
const proxyGlob = [
    '**'
]
const proxyConfig = {
    target: BROWSERSYNC_TARGET,
}
const proxyMw = proxyMiddleware(proxyGlob, proxyConfig)


// ..CONFIG
// =================
export default {
    port: 3000,
    host: '0.0.0.0',
    open: false,
    watch: true,
    server: {
        middleware: [
            webpackMw,
            proxyMw
        ]
    }
}