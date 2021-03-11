function post1(sentence, cb){
  axios.post('http://34.72.172.211:8000/predict', {"sentence": sentence})
  // axios.post('http://localhost:8000/predict', {"sentence": sentence})
    .then(res => cb(res.data))
// fetch('http://34.72.172.211:8000/predict', {
//     method: 'POST',
//     headers: {
//         'accept': 'application/json',
//         'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({"sentence": sentence})
// }).then(response=>{
//   response.json().then(cb)
// });
}