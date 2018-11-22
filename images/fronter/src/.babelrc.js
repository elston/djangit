module.exports = {

  // PRESETS
  presets: [[
    // ..preset-env
    // ..
    '@babel/preset-env', {
      targets: {
        node: 'current'
      }
    }

  ],[
    // ..preset-flow
    // ..
    '@babel/preset-flow'  

  ]],

  // PLUGINS
  plugins: [[
    // ...
    '@babel/plugin-proposal-decorators', {
      'legacy': true 
    }
    
  ]],

  // IGNORE
  ignore: [
    'node_modules', 
    'build'
  ],

};