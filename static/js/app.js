// Creating a function to create the heart failure table

function buildtable1() {

  /* data route */
  let url1 = "/api/data";

  var tbody1 = d3.select(".heart-table");

  d3.json(url1).then(function(data) {

    data.forEach((item) => {
      let row = tbody1.append("tr")
      let age = row.append("td")
      let anaemia = row.append("td")
      let creatinine_phosphokinase = row.append("td")
      let diabetes = row.append("td")
      let ejection_fraction = row.append("td")
      let high_blood_pressure = row.append("td")
      let platelets = row.append("td")
      let serum_creatinine = row.append("td")
      let serum_sodium = row.append("td")
      let sex = row.append("td")
      let smoking = row.append("td")
      let time = row.append("td")
      let death_event = row.append("td")

      age.text(item.Age);
      anaemia.text(item.Anaemia);
      creatinine_phosphokinase.text(item.Creatinine_phosphokinase);
      diabetes.text(item.Diabetes);
      ejection_fraction.text(item.Ejection_fraction);
      high_blood_pressure.text(item.High_blood_pressure);
      platelets.text(item.Platelets);
      serum_creatinine.text(item.Serum_creatinine);
      serum_sodium.text(item.Serum_sodium);
      sex.text(item.Sex);
      smoking.text(item.Smoking);
      time.text(item.Time);
      death_event.text(item.Death_event);

    })

  })

}

buildtable1();




// Creating a function to create the F1 Score table

function buildtable2() {

  /* data route */
  let url2 = "/api/f1score";
  console.log(url2)

  var tbody2 = d3.select(".f1-table");

  d3.json(url2).then(function(data) {

    data.forEach((item) => {
      let row = tbody2.append("tr")
      let index = row.append("td")
      let precision = row.append("td")
      let recall = row.append("td")
      let f1score = row.append("td")
      let support = row.append("td")


      index.text(item.Index);
      precision.text(item.Precision);
      recall.text(item.Recall);
      f1score.text(item.F1_score);
      support.text(item.Support);

    })

  })

}

buildtable2();












