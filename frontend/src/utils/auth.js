export function checkToken(props){
  let token =null;

  if(props.token!=null){
    token=props.token;
  }
  else{
    const cookies = document.cookie.split(";").reduce((cookies, cookie) => {
      const [name, value] = cookie.trim().split("=");
      return { ...cookies, [name]: value };
    }, {});

    if (cookies==null || cookies.token==null) {
      window.location.replace('/login');
      return null;
    }

    token=cookies.token;
  }

  console.log("token: "+ token);
  return token;

};


//TODO figure out how to send the token as header in all api calls so we can also check the auth of each call

