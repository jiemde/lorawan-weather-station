var resources = payload.toString("ascii").split(" ");
return {
   temperature: resources[0],
   pressure: resources[1],
   humidity: resources[2],
   speed: resources[3],
   direction: resources[4]
};
