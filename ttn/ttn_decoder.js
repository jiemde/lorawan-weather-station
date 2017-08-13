// example how to decode the payload

function Decoder(bytes, port) {

  var resources = String.fromCharCode.apply(null, bytes).split(" ");

  return {
     temp: resources[0],
     hum: resources[1],
     airpressure: resources[2],
     windspeed: resources[3],
     winddir: resources[4],
     batteryvolt: resources[5]
  };

}
