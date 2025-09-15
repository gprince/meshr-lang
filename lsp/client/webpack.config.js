const path = require('path');

module.exports = {
    entry: './src/extension_lsp_debug.ts',
    target: 'node',
    mode: 'production',
    module: {
        rules: [
            {
                test: /\.ts$/,
                use: 'ts-loader',
                exclude: /node_modules/,
            },
        ],
    },
    resolve: {
        extensions: ['.ts', '.js'],
        alias: {
            'vscode-languageclient': path.resolve(__dirname, 'node_modules/vscode-languageclient'),
            'vscode-languageserver-protocol': path.resolve(__dirname, 'node_modules/vscode-languageserver-protocol'),
            'vscode-jsonrpc': path.resolve(__dirname, 'node_modules/vscode-jsonrpc'),
            'vscode-languageserver-types': path.resolve(__dirname, 'node_modules/vscode-languageserver-types'),
        },
    },
    output: {
        filename: 'extension_bundled.js',
        path: path.resolve(__dirname, 'out'),
        libraryTarget: 'commonjs2',
    },
    externals: {
        vscode: 'commonjs vscode',
    },
    optimization: {
        minimize: false,
    },
};

