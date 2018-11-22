import path from 'path'


// ...mode
export const DEBUG = !process.argv.includes('--release')
export const QUIET = process.argv.includes('--quiet')
export const SSR = process.argv.includes('--ssr')

// .. server
export const BROWSERSYNC_HOST = process.env.BROWSERSYNC_HOST
export const BROWSERSYNC_PORT = process.env.BROWSERSYNC_PORT
export const BROWSERSYNC_TARGET = process.env.BROWSERSYNC_TARGET


// ... dirs
export const ROOT_DIR = path.resolve(__dirname, '..')
export const resolvePath = (...args) => (
    path.resolve(ROOT_DIR, ...args)
)

// ...
export const SRC_DIR = resolvePath('src')
export const BUILD_DIR = resolvePath('build')
// ..