import * as pragmajs from "pragmajs"
import styles from "./styles.json"
import icons from "./icons.json"

function injectStyle(name){
    if (! name in styles) return console.error(`could not find ${name}.scss in website/src/styles`) 
    pragmajs.util.addStyles(styles[name])
}

function SVG(name, fill) {
    if (! name in icons) return console.error(`could not find ${name}.scss in website/src/styles`)
    let i = icons[name]
    if (fill) return pragmajs._e(i).css(`fill ${fill}`).html()
    return i
}


function compose(){
    let _page = _p().as('body')
    console.time()
    _page.element.findAll("[pragma]").forEach(element => {
        let pragmas = new Map

        Object.keys(element.attributes).filter(v => {
            return element.attributes[v].name[0] == "#"
        }).forEach(v => pragmas.set(element.attributes[v].name.slice(1), element))

        for (let [key, element] of pragmas) {
            _page.adopt(
                _p(key)
                    .as(element.setId(key))
                    .run(function() {
                        _page[util.snake2camel(key)] = this
                    })
            )

            console.timeLog()
        }
        
    })

    _page.element.findAll("[element]").forEach(element => {
        let elements = new Map

        Object.keys(element.attributes).filter(v => {
            return element.attributes[v].name[0] == "#"
        }).forEach(v => elements.set(element.attributes[v].name.slice(1), element))

        for (let [key, element] of elements) {
            _page.adopt(
                _e(element)
                    .setId(key)
            )
        }
    })

    console.timeEnd()
    window._page = _page
}

// globalifying pragma, and functions
for (let [key, val] of Object.entries({ ...pragmajs, ...{ injectStyle, SVG, compose } })) {
    window[key] = val
}

export { icons, styles, SVG, injectStyle, pragmajs, compose }
