const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');


module.exports = {
    mode: "development",
    context: __dirname,
    entry: path.resolve(__dirname, 'bookit/assets/js/index.js'),
    output: {
        path: path.resolve(__dirname, 'bookit/assets/dist/'),
        filename: "[name].[hash].js"
    },
    plugins: [
        new webpack.ProvidePlugin(
            {
                $: 'jquery',
                jQuery: 'jquery',
                'windows.jQuery': 'jquery',
            }
        ),
        new webpack.SourceMapDevToolPlugin({exclude: ['popper.js']}),
        new CleanWebpackPlugin(),
        new BundleTracker({filename: 'bookit/webpack-stats.json'})
    ],
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: 
                [
                    "style-loader", //3. load styles into dom
                    "css-loader", //2. turn css into js
                    "sass-loader" //1. turn sass into css 
                ]
            }
        ]
    },
    resolve: {
        alias: {
            // Force all modules to use the same jquery version.
            'jquery': path.join(__dirname, 'node_modules/jquery/src/jquery')
        },
        modules: ['node_modules']
    }
};
