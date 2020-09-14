// var username = getCookie('username');
// if (username) {
//     var user = document.getElementById('username');
//     var _user = document.getElementById('_username');
//     user.innerText = username;
//     _user.innerText = username;
// } else {
//     location.href = './login.html'
// }
var menu = document.querySelector('.menu');
var ifram = document.getElementsByTagName('iframe')[0];
menu.onclick = function(e){
    var event = e || window.event;
    var target  = event.target || event.srcElement;
    if(target.tagName == 'DD'){
        target.classList.add('active');
        var siblings = getSiblings(target);
        for (var i = 0; i < siblings.length; i++) {
            siblings[i].classList.remove('active');
        };
        var id = target.getAttribute('data-id');
        var data = '/'+id+'/';
        ifram.setAttribute('src',data);
    };
};
//获取兄弟节点
function getSiblings(node){
    var parentNode = node.parentNode;
    var children = parentNode.children;
    var result = [];
    for(var i = 0;i < children.length;i ++){
        if(node != children[i]){
            result.push(children[i])
        }
    };
    return result;
};