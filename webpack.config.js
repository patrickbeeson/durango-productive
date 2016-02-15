const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,

  entry: {
    Home: './durangoproductive/static/js/components/home.jsx',
    Projects: './durangoproductive/static/js/components/projects.jsx',
    Project: './durangoproductive/static/js/components/project.jsx',
    Contact: './durangoproductive/static/js/components/contact.jsx',
  },

  output: {
      path: path.resolve('./durangoproductive/static/bundles/'),
      filename: "[name]-[hash].js",
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
  ],

  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
    ],
  },

  resolve: {
    modulesDirectories: ['node_modules', 'bower_components'],
    extensions: ['', '.js', '.jsx']
  },
}
