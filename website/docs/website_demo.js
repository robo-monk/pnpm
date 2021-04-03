website.compose() // creates the _page object with all the pragmas defined in the html
website.injectStyle('main')

console.log(website.displayWrapper)
console.log(website.display)

_page.display
    .css("height 250px")
    .createWire('icon')
    .on('iconChange', function (v) {
        if (this._last) this._last.destroy()
        this._last = _e(website.icons[this._icons[v]])
            .addClass('fade-onload')
            .css('fill whitesmoke')
            .appendTo(this)
    })
    .run(function () {
        this._icons = Object.keys(website.icons)
        this.setIconLoop(0, this._icons.length - 1)
        setInterval(() => {
            this.icon++
        }, 420+69);
    })
    .setIcon(0)
