export interface UserFieldGroup {
    name: string;
    id: string;
    fields?: Array<any>
  }
  export interface Workspace {
    name: string;
    id: string;
    field_groups?: Array<UserFieldGroup>
  }
  