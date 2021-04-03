__pkg__.compose() // creates the _page object with all the pragmas defined in the html
__pkg__.injectStyle('main')

console.log(__pkg__.displayWrapper)
console.log(__pkg__.display)

_page.display
    .css("height 250px")
    .createWire('icon')
    .on('iconChange', function (v) {
        if (this._last) this._last.destroy()
        this._last = _e(shit.icons[this._icons[v]])
            .addClass('fade-onload')
            .css('fill whitesmoke')
            .appendTo(this)
    })
    .run(function () {
        this._icons = Object.keys(shit.icons)
        this.setIconLoop(0, this._icons.length - 1)
        setInterval(() => {
            this.icon++
        }, 500);
    })
    .setIcon(0)
