const path = require('path');
const { watch } = require('vue');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  publicPath: 'http://127.0.0.1:8000/',

  chainWebpack: config => {
    config.plugin('BundleTracker').use(BundleTracker, [{ filename: 'webpack-stats.json' }]);
    config.output.filename('bundle.js');
    config.optimization.splitChunks(false);
    config.resolve.alias.set('__STATIC__', 'static');
  },

  devServer: {
    hot: true,
  },

  configureWebpack: {
    resolve: {
      extensions: ['.ts', '.js', '.vue', '.json'],
    },
    module: {
      rules: [
        {
          test: /\.ts$/,
          loader: 'ts-loader',
          options: {
            appendTsSuffixTo: [/\.vue$/],
            transpileOnly: true,
          },
          exclude: /node_modules/,
        },
      ],
    },
  },
};
