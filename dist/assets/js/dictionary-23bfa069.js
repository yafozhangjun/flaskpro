import{bM as s,bN as r,__tla as o}from"./index-acc4e75c.js";import{d as c,__tla as n}from"./index-d768e128.js";import{d as e,__tla as _}from"./index-6dde14d2.js";let i,l=Promise.all([(()=>{try{return o}catch{}})(),(()=>{try{return n}catch{}})(),(()=>{try{return _}catch{}})()]).then(async()=>{i=s({id:"dictionary",state:()=>({stationList:[],realDataList:[],dictionaryList:[]}),getters:{stationListGet:t=>t.stationList,realDataListGet:t=>t.realDataList,dictionaryListGet:t=>t.dictionaryList},actions:{async getStationList(){const{success:t,data:{list:a}}=await c();t&&(this.stationList=a)},setDictionaryList(t){this.dictionaryList=t},async getDictionaryList(){const{success:t,data:a}=await e();t&&(this.dictionaryList=a)}},persist:r("dictionary")})});export{l as __tla,i as u};