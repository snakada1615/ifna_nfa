//Open new IndexedDB conncetion.
var dbPromise = idb.open('feeds-db', 5, function(upgradeDb) {
  upgradeDb.createObjectStore('feeds',{keyPath:'pk'});
});

//collect latest post from server and store in idb.
fetch('http://127.0.0.1:8000/getdata').then(function(response){
  return response.json();
}).then(function(jsondata){
  dbPromise.then(function(db){
    var tx = db.transaction('feeds', 'readwrite');
      var feedsStore = tx.objectStore('feeds');
      for(var key in jsondata){
        if (jsondata.hasOwnProperty(key)) {
          feedsStore.put(jsondata[key]);
        }
      }
  });
});

//retrive data from idb and display on page.
var post="";
dbPromise.then(function(db){
  var tx = db.transaction('feeds', 'readonly');
    var feedsStore = tx.objectStore('feeds');
    return feedsStore.openCursor();
}).then(function logItems(cursor) {
    if (!cursor) {
      //if true means we are done cursoring over all records in feeds.
      document.getElementById('offlinedata').innerHTML=post;
      return;
    }
    for (var field in cursor.value) {
        if(field=='fields'){
          feedsData=cursor.value[field];
          for(var key in feedsData){
            if(key =='Food_name'){
              var Food_name = '<h3>'+feedsData[key]+'</h3>';
            }
            if(key =='Food_grp'){
              var Food_grp = feedsData[key];
            }
            if(key == 'Protein'){
              var Protein = '<p>'+feedsData[key]+'</p>';
            }
          }
          post=post+'<br>'+Food_name+'<br>'+Food_grp+'<br>'+Protein+'<br>';
        }
      }
    return cursor.continue().then(logItems);
  });
