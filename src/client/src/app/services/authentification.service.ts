import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';

export interface User {
  email: string,
  id: string,
  first_name: string,
  last_name: string
}
export interface AuthenticationInfo {
  user: User,
  token: string
}
@Injectable()
export class AuthentificationService {
  public authInfo: AuthenticationInfo = { token: '',user:null }
  constructor(private http: Http) { }

  setInfo(info:AuthenticationInfo) {
    this.authInfo = info;    
  }
  login(email: string, password: string): Observable<AuthenticationInfo> {
    return this.http.post('http://localhost:5050/api/login', { email: email, password: btoa(password) }).map(login_info => login_info.json());
  }

  verify(): Observable<AuthenticationInfo> {
    let headers = new Headers();
    headers.append("Authorization", "Basic " + btoa(this.authInfo.token + ":unused"));
    return this.http.get('http://localhost:5050/api/login', { headers: headers }).map(login_info => login_info.json());
  }
  getUser(): Observable<User> {
    let headers = new Headers();
    headers.append("Authorization", "Basic " + btoa(this.authInfo.token + ":unused"));
    return this.http.get('http://localhost:5050/api/user', { headers: headers }).map(user_info => user_info.json());
  }
  saveUser(user:User):Observable<User> {
    console.log(user)
    let headers = new Headers();
    headers.append("Authorization", "Basic " + btoa(this.authInfo.token + ":unused"));
    return this.http.put('http://localhost:5050/api/user', user, { headers: headers }).map(user_info => user_info.json());
    
  }
}
