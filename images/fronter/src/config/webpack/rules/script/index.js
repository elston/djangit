import { 
    DEBUG, 
    SRC_DIR } from '../../../consts'
import { 
    reScript, 
    minimizeCssOptions,
    browsersList } from '../consts' 
    
// ...
const config = {}

// ..COMMON
// ================================
// ..
config['test'] = reScript
config['include'] = SRC_DIR
config['loader'] = 'babel-loader'


// .. OPTIONS
// ================================
config['options'] = {}
// ..
// options.cacheDirectory = DEBUG
config.options['babelrc'] = false


// .. PRESETS
// ================================
config.options['presets'] = [[
    
    // ..preset-env
    // ..
    "@babel/preset-env", {
        targets: {
            browsers: browsersList,
        },
        forceAllTransforms: !DEBUG,
        modules: false,
        useBuiltIns: false,
        debug: false,
    }
],[
    // ..preset-react
    // ..
    '@babel/preset-react', { 
        development: DEBUG
    }
],[
    // ..preset-flow
    // ..
    '@babel/preset-flow'

]]



// .. PLUGINS
// ================================
config.options['plugins'] = [[

    // .. plugin-proposal-decorators
    // ..
    '@babel/plugin-proposal-decorators', {
        'legacy': true 
    }
]]


// ..
export default config