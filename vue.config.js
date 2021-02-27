module.exports = {
  runtimeCompiler: true,
  chainWebpack: config =>  {
    if (process.env.NODE_ENV === 'production') {
    }
    else if (process.env.NODE_ENV === 'development') {
      config.plugin('html').tap(args => {
        args[0].minify = {
          removeComments: true,
          collapseWhitespace: true,
          collapseBooleanAttributes: true,
          removeScriptTypeAttributes: true,
        };
        return args;
      });
    }
  },
}
