import{bD as J,d as E,o as I,e as $,bC as R,n as j,_ as z,C as P,r as g,u as S,bE as O,G as Q,q as X,a as C,m as Y,bF as Z,b as d,h as s,w as t,x as h,K as M,f as ee,i as q,bG as ae,bH as se,F as te,bI as D,bJ as re,bK as oe,bL as le,__tla as ie}from"./index-acc4e75c.js";import{u as ne,a as de,__tla as ue}from"./keepAlive-ca6182d7.js";import{u as ce,__tla as me}from"./dictionary-23bfa069.js";import{__tla as pe}from"./index-d768e128.js";import{__tla as _e}from"./index-6dde14d2.js";let H,fe=Promise.all([(()=>{try{return ie}catch{}})(),(()=>{try{return ue}catch{}})(),(()=>{try{return me}catch{}})(),(()=>{try{return pe}catch{}})(),(()=>{try{return _e}catch{}})()]).then(async()=>{let y,b,w;y=[j('<div class="eyes" data-v-42fe1c79></div><div class="arm-up-right" data-v-42fe1c79></div><div class="arm-up-left" data-v-42fe1c79></div><div class="arm-down-left" data-v-42fe1c79></div><div class="arm-down-right" data-v-42fe1c79></div>',5)],b=z(E({__name:"index",props:{passWord:{type:Boolean,default:!0}},setup:K=>(o,r)=>(I(),$("div",{class:R(["owl-login",o.passWord?"passWord":""])},y,2))}),[["__scopeId","data-v-42fe1c79"]]),w={class:"login-btn"},H=z(E({__name:"loginForm",setup(K){const{t:o}=P();let r=g(!1);const U=S(),W=O(),B=ne(),k=ce(),G=de(),T=Q();X(()=>T.isLogo);const m=g(),A=C({userName:[{required:!0,message:"\u8BF7\u8F93\u5165\u7528\u6237\u540D",trigger:"blur"}],passWord:[{required:!0,message:"\u8BF7\u8F93\u5165\u5BC6\u7801",trigger:"blur"}]}),c=g(!1),u=C({userName:"",passWord:""}),L=()=>{let e=new Date().getHours();return e>=6&&e<=10?`${o("hello.morning")} \u26C5`:e>=10&&e<=14?`${o("hello.afternoon")} \u{1F31E}`:e>=14&&e<=18?`${o("hello.xiawu")} \u{1F31E}`:e>=18&&e<=24?`${o("hello.evening")} \u{1F31B}`:e>=0&&e<=6?`${o("hello.hours")} \u{1F31B}`:void 0},N=e=>{if(e)try{e.validate(async a=>{if(!a)return;c.value=!0;const{success:f,message:p,data:l}=await(i=>J.post("/login",i))(u);if(l&&(W.setToken(l.token),W.setUserInfo(l)),!f||!l.token)return D({title:L(),message:p,type:"error",duration:3e3}),void(c.value=!1);await k.getStationList(),k.getDictionaryList(),await re(),B.closeMultipleTab(),G.setKeepAliveName();const{authMenuList:_}=oe(),v=le(_).find(i=>i.name!="home"&&!i.meta.isHide&&!i.redirect);U.push({name:v.name||"monitoring"}),D({title:L(),message:"\u6B22\u8FCE\u767B\u9646\u4E1C\u6797\u5BFA\u6302\u5355\u7CFB\u7EDF",type:"success",duration:3e3})})}catch{}finally{c.value=!1}},x=e=>{if((e=window.event||e).code==="Enter"||e.code==="enter"||e.code==="NumpadEnter"){if(c.value)return;N(m.value)}};return Y(()=>{document.addEventListener("keydown",x)}),Z(()=>{document.removeEventListener("keydown",x)}),(e,a)=>{const f=d("user"),p=d("el-icon"),l=d("el-input"),_=d("el-form-item"),v=d("lock"),i=d("el-form"),F=d("el-button");return I(),$(te,null,[s(i,{ref_key:"loginFormRef",ref:m,model:u,rules:A,size:"large"},{default:t(()=>[s(b,{passWord:h(r)},null,8,["passWord"]),s(_,{prop:"userName",class:"login-user"},{default:t(()=>[s(l,{modelValue:u.userName,"onUpdate:modelValue":a[0]||(a[0]=n=>u.userName=n),modelModifiers:{trim:!0},placeholder:"\u8BF7\u8F93\u5165\u7528\u6237\u540D"},{prefix:t(()=>[s(p,{class:"el-input__icon"},{default:t(()=>[s(f)]),_:1})]),_:1},8,["modelValue"])]),_:1}),s(_,{prop:"passWord"},{default:t(()=>[s(l,{type:"passWord",modelValue:u.passWord,"onUpdate:modelValue":a[1]||(a[1]=n=>u.passWord=n),modelModifiers:{trim:!0},placeholder:"\u8BF7\u8F93\u5165\u5BC6\u7801","show-passWord":"",autocomplete:"new-passWord",onFocus:a[2]||(a[2]=n=>M(r)?r.value=!0:r=!0),onBlur:a[3]||(a[3]=n=>M(r)?r.value=!1:r=!1)},{prefix:t(()=>[s(p,{class:"el-input__icon"},{default:t(()=>[s(v)]),_:1})]),_:1},8,["modelValue"])]),_:1})]),_:1},8,["model","rules"]),ee("div",w,[s(F,{icon:h(ae),round:"",onClick:a[4]||(a[4]=n=>{var V;(V=m.value)&&V.resetFields()}),size:"large"},{default:t(()=>[q("\u91CD\u7F6E")]),_:1},8,["icon"]),s(F,{icon:h(se),round:"",onClick:a[5]||(a[5]=n=>N(m.value)),size:"large",type:"primary",loading:c.value},{default:t(()=>[q(" \u767B\u5F55 ")]),_:1},8,["icon","loading"])])],64)}}}),[["__scopeId","data-v-b24fdb0c"]])});export{fe as __tla,H as default};