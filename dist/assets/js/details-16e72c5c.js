import{b as ce,s as ie,c as pe,__tla as ve}from"./index-a4298109.js";import{d as fe,C as me,G as he,r as v,c as _e,a as ge,D as q,m as be,b as c,o as P,j as R,w as t,f as I,h as s,i as b,t as _,x as d,K as ye,bQ as ke,bJ as xe,J as A,H as Ne,_ as Ce,__tla as Ve}from"./index-acc4e75c.js";import{u as we,a as Me,__tla as Ie}from"./keepAlive-ca6182d7.js";let D,$e=Promise.all([(()=>{try{return ve}catch{}})(),(()=>{try{return Ve}catch{}})(),(()=>{try{return Ie}catch{}})()]).then(async()=>{let $;$={class:"custom-tree-node"},D=Ce(fe({__name:"details",setup(Oe,{expose:E}){const{t:u}=me();he();const y=v(!0),O=v(u("toolsManagement.all_text")),C=v(""),{userInfo:{userId:F}}=_e.get("userInfo"),G={label:"title"};let k=v("one");const g=v(!1),U=v(),H=we(),L=Me(),Q=ge({title:[{required:!0,message:u("search.placeholder"),trigger:"blur"}],status:[{required:!0,message:u("search.select"),trigger:"blur"}]}),m=v({}),f=v({row:{},title:""}),h=v(),J=v([]);let x=v(!1);const V=v([]),T=v([]);q(C,l=>{h.value.filter(l)});const z=()=>{y.value=!y.value,O.value=y.value?u("toolsManagement.all_text"):u("toolsManagement.no_text");let l=h.value.store.nodesMap;for(let e in l)l[e].expanded=y.value},B=(l,e,a)=>{if(!l)return!0;let n=a.parent,r=[a.label],i=1;for(;i<a.level;)r=[...r,n.label],n=n.parent,i++;return r.some(o=>o.indexOf(l)!==-1)},W=(l,e)=>{k.value=l.paneName},X=()=>{g.value=!1},w=(l,e,a)=>{let n=l.children,r=n.length;a.setChecked(l.id,e);for(let i=0;i<r;i++)w(n[i],e,a)},K=(l,e)=>{let a=e.getNode(l);if(a.parent.key!==void 0)return e.setChecked(a.parent,!0),K(a.parent,e)},M=(l,e)=>{let a=0,n=0,r=0,i=0,o=e.getNode(l);if(o.parent!==null&&o.parent.key!==void 0&&(e.setChecked(o.parent,!0),M(o.parent,e)),o.childNodes.length!==0){for(;r<o.childNodes.length;r++)if(o.childNodes[r].checked===!1&&++a,a===o.childNodes.length&&o.childNodes[r].parent.key!==void 0)for(e.setChecked(o.childNodes[r].parent,!1),i=0;i<o.parent.childNodes.length;i++)o.parent.childNodes[i].checked===!1&&++n,n===o.parent.childNodes.length&&(e.setChecked(o.parent.key,!1),Ne(()=>M(o.parent,e)))}},Y=(l,e)=>{e.checkedKeys.indexOf(l.id)!==-1?(K(l,h.value),w(l,!0,h.value)):(l.parentId!==-1&&M(l,h.value),l.children.length!==0&&w(l,!1,h.value))},Z=()=>{var l;(l=U.value)==null||l.validate(async e=>{if(!e)return;let a=null;try{m.value.rules=h.value.getCheckedNodes(!1,!0).map(n=>n.id).join(","),f.value.title=="\u65B0\u589E"?(m.value.userId=F,a=await ce(m.value)):f.value.title=="\u7F16\u8F91"&&(a=await ie(m.value)),await xe(),H.closeMultipleTab(),L.setKeepAliveName(),a.success?A.success({message:`${f.value.title=="\u7F16\u8F91"?u("excel.edit"):u("excel.add")}${u("excel.success")}`}):A.error(`${a.message}`),f.value.getTableList(),g.value=!1}catch{}})},S=l=>[].concat(...l.map(e=>{if(e.children){let a=[].concat(e,S(e.children));return delete e.children,a}return[].concat(e)})),ee=()=>{x.value?h.value.setCheckedNodes([]):h.value.setCheckedNodes(T.value),x.value=!x.value};return be(()=>{(async()=>{const{success:l,data:{list:e}}=await pe();if(!l)return;J.value=e;let a=JSON.parse(JSON.stringify(e));T.value=S(a)})()}),q(g,l=>{var e,a;l&&(f.value.title=="\u7F16\u8F91"?(m.value=f.value.row,V.value=(e=f.value.row)==null?void 0:e.rules.split(",")):f.value.title=="\u65B0\u589E"&&(m.value={},V.value=[]),x.value=!!((a=f.value.row)!=null&&a.rules))}),E({acceptParams:l=>{f.value=l,g.value=!0}}),(l,e)=>{const a=c("el-input"),n=c("el-form-item"),r=c("el-col"),i=c("el-radio-button"),o=c("el-radio-group"),N=c("el-button"),le=c("el-icon"),ae=c("el-tree"),te=c("el-scrollbar"),j=c("el-row"),se=c("el-container"),ue=c("el-card"),oe=c("el-form"),de=c("el-tab-pane"),re=c("el-tabs"),ne=c("el-drawer");return P(),R(ne,{modelValue:g.value,"onUpdate:modelValue":e[4]||(e[4]=p=>g.value=p),"destroy-on-close":!0,size:"90%",title:`${f.value.title=="\u7F16\u8F91"?d(u)("excel.edit"):d(u)("excel.add")}${d(u)("toolsManagement.tool")}`},{footer:t(()=>[I("div",null,[s(N,{type:"primary",onClick:Z},{default:t(()=>[b(_(d(u)("excel.submit")),1)]),_:1}),s(N,{onClick:X},{default:t(()=>[b(_(d(u)("excel.cancel")),1)]),_:1})])]),default:t(()=>[s(re,{type:"border-card",class:"demo-tabs",onTabClick:W,modelValue:d(k),"onUpdate:modelValue":e[3]||(e[3]=p=>ye(k)?k.value=p:k=p)},{default:t(()=>[s(de,{label:`${f.value.title=="\u7F16\u8F91"?d(u)("excel.edit"):d(u)("excel.add")}${d(u)("toolsManagement.tool")}`,name:"one"},{default:t(()=>[s(oe,{model:m.value,rules:Q,ref_key:"ruleFormRef",ref:U,"label-position":"left","label-width":"auto"},{default:t(()=>[s(j,{gutter:70},{default:t(()=>[s(r,{span:12},{default:t(()=>[s(n,{label:d(u)("toolsManagement.title"),prop:"title"},{default:t(()=>[s(a,{modelValue:m.value.title,"onUpdate:modelValue":e[0]||(e[0]=p=>m.value.title=p)},null,8,["modelValue"])]),_:1},8,["label"])]),_:1}),s(r,{span:12},{default:t(()=>[s(n,{label:d(u)("toolsManagement.isStatus"),prop:"status"},{default:t(()=>[s(o,{modelValue:m.value.status,"onUpdate:modelValue":e[1]||(e[1]=p=>m.value.status=p)},{default:t(()=>[s(i,{label:1},{default:t(()=>[b(_(d(u)("toolsManagement.yes")),1)]),_:1}),s(i,{label:0},{default:t(()=>[b(_(d(u)("toolsManagement.no")),1)]),_:1})]),_:1},8,["modelValue"])]),_:1},8,["label"])]),_:1}),s(r,{span:24},{default:t(()=>[s(n,{label:d(u)("toolsManagement.user_tool")},{default:t(()=>[s(ue,null,{default:t(()=>[s(se,null,{default:t(()=>[s(j,null,{default:t(()=>[s(r,{span:24},{default:t(()=>[s(N,{type:"primary",size:"small",onClick:ee},{default:t(()=>[b(_(d(x)?d(u)("excel.reset_all"):d(u)("excel.all")),1)]),_:1}),s(N,{type:"primary",size:"small",onClick:z},{default:t(()=>[b(_(O.value),1)]),_:1})]),_:1}),s(r,{span:24},{default:t(()=>[s(te,{height:"500px"},{default:t(()=>[s(a,{modelValue:C.value,"onUpdate:modelValue":e[2]||(e[2]=p=>C.value=p),placeholder:d(u)("search.placeholder"),style:{marginTop:"10px"}},null,8,["modelValue","placeholder"]),s(ae,{ref_key:"tree",ref:h,props:G,data:J.value,"show-checkbox":"","node-key":"id","default-checked-keys":V.value,"default-expand-all":y.value,"highlight-current":"",style:{"margin-top":"10px"},"check-strictly":"",onCheck:Y,"filter-node-method":B,onNodeExpand:z},{default:t(({node:p,data:Ue})=>[I("span",$,[s(le,{style:{marginRight:"5px"}},{default:t(()=>[(P(),R(ke(p.data.icon)))]),_:2},1024),I("span",null,_(p.label),1)])]),_:1},8,["data","default-checked-keys","default-expand-all"])]),_:1})]),_:1})]),_:1})]),_:1})]),_:1})]),_:1},8,["label"])]),_:1})]),_:1})]),_:1},8,["model","rules"])]),_:1},8,["label"])]),_:1},8,["modelValue"])]),_:1},8,["modelValue","title"])}}}),[["__scopeId","data-v-7f9cece1"]])});export{$e as __tla,D as default};