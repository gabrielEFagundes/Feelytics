import bcrypt, { hash } from 'bcryptjs';

export function hashPass(pass){
    const salt = bcrypt.genSaltSync(10);

    return bcrypt.hashSync(pass, salt);
}