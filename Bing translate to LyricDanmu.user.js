// ==UserScript==
// @name         Bing translate to LyricDanmu
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  将语音输入内容转发至LyricDanmu
// @author       c_basalt
// @match        https://www.bing.com/translator*
// @grant        GM_xmlhttpRequest
// ==/UserScript==

(function() {
    'use strict';

    const regexFixes = [
        [/下厨/g, '夏厨'],
        [/[卡夏像下][诺洛路][尔亚雅]/g, '夏诺雅'],
        [/(NOA|nova|noah|nua|no啊|诺尔)/g, 'noa'],
        [/鼓手/g, '古守'],
        [/灵宝/g, '铃宝'],
        [/林强/g, '铃酱'],
    ]

    const jsonPost = function (data) {
        GM_xmlhttpRequest({
            method: "post",
            url: "http://127.0.0.1:8745/control",
            headers: { "Content-Type": "application/json;charset=UTF-8" },
            data: JSON.stringify(data)
        })
    }
    let inputArea = null;
    const postText = function () {
        jsonPost({
            command: "set_comment",
            payload: {
                text: inputArea.value
            }
        })
    }
    const _fixInput = function() {
        const inputArea = document.querySelector('#tta_input_ta');
        let text = inputArea.value;
        regexFixes.forEach( i=>{ text = text.replaceAll(i[0], i[1]) } )
        inputArea.value = text;
    }
    const fixInput = function() {
        const i = setInterval(_fixInput, 100)
        setTimeout(()=>{clearInterval(i)}, 1500);
    }
    const init = function() {
        inputArea = document.querySelector('#tta_input_ta');
        if (!inputArea) {
            setTimeout(init, 500);
        } else {
            setInterval(postText, 200);
            const observer = new MutationObserver(fixInput);
            observer.observe(document.querySelector('#tta_speechiconsrc .ovr_cont'), { childList:true, subtree: true });
        }
    }
    init()
})();