(function (global, factory) {
    typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports) :
    typeof define === 'function' && define.amd ? define(['exports'], factory) :
    (global = typeof globalThis !== 'undefined' ? globalThis : global || self, factory(global.__pkg__ = {}));
}(this, (function (exports) { 'use strict';

    function __pkg__Test(){
        console.log("hello from ___pkg__");
    }

    exports.__pkg__Test = __pkg__Test;

    Object.defineProperty(exports, '__esModule', { value: true });

})));
