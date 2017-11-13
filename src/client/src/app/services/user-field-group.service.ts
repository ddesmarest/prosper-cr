import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';

import { AuthenticatedService } from './authenticated-service';
import { AuthentificationService } from './authentification.service';

import { Workspace,UserFieldGroup } from './data-model';
export { Workspace,UserFieldGroup } from './data-model';

@Injectable()
export class UserFieldGroupService extends AuthenticatedService {

  constructor(private http: Http, authService: AuthentificationService) {
    super(authService);
  }
  getUserFieldGroups(workspace:Workspace): Observable<Array<Workspace>> {
    return this.http.get(this.getFullUrl('workspaces',workspace.id,'field-groups'), { headers: this.createHeaders() }).map(groups => groups.json());
  }

}
