var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  context: __dirname,

  entry: {
    header: "./frontend/static/js/header",
  },

  output: {
    path: path.resolve("./frontend/static/js/bundles/"),
    filename: "[name].js",
  },

  plugins: [new BundleTracker({ filename: "./webpack-stats.json" })],
  module: {
    rules: [
      {
        test: /\.jsx$/,
        exclude: /node_modules/,
        use: ["babel-loader"],
      },
    ],
  },
  resolve: {
    extensions: ["*", ".js", ".jsx"],
  },
  optimization: {
    splitChunks: {
      // include all types of chunks
      chunks: "all",
    },
  },
};
