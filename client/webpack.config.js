const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const {CleanWebpackPlugin} = require("clean-webpack-plugin");
const webpack = require("webpack");

module.exports = {
  mode: "development",
  devtool: "inline-source-map",
  devServer: {
    contentBase: "./dist"
  },
  entry: {
    app: "./src/js/index.js"
  },
  output: {
    filename: "[name].bundle.js",
    path: path.resolve(__dirname, "dist"),
    publicPath: "/"
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      title: "$1"
    }),
    new webpack.HotModuleReplacementPlugin()
  ],
  resolve: {
    extensions: [".js"]
  }
};
