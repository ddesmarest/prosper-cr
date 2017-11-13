import { AuthentificationService } from './authentification.service';
import { Headers } from '@angular/http';
export class AuthenticatedService {
    constructor( protected authService:AuthentificationService) {
    }
    protected createHeaders(): Headers {
        let headers = new Headers();
        headers.append("Authorization", "Basic " + btoa(this.authService.authInfo.token + ":unused"));
        return headers;
    }
    protected getFullUrl(...api_url:string[]) {
        return 'http://localhost:5050/api/'+api_url.join('/');
    }
}