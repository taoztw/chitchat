<template>
<div id="app">
	<!-- <img src="./assets/logo.png"> -->
	<router-view></router-view>
</div>
</template>

<style  type="text/css">
*,
*:after,
*:before {
    max-height: 100000px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    // -webkit-tap-highlight-color: rgba(0,0,0,0);
    // -ms-touch-action: none;
    // -webkit-touch-callout: none;
    // user-select: none;
    // text-size-adjust: none;
}

body,
html {
    background-color: #F5F6F8;
    width: 100%;
    height: 100%;
    font-family: 'Microsoft Yahei' !important;
}

::-webkit-scrollbar {
    width: 2px;
    height: 2px;
}

::-webkit-scrollbar-track {
    background: transparent;
}

::-webkit-scrollbar-thumb {
    background: rgba(0, 0, 0, .1);
}

.icon {
    width: 1.2em;
    height: 1.2em;
    vertical-align: -0.3em;
    fill: currentColor;
    overflow: hidden;
}
</style>
