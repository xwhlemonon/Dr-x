import * as React from "react";
import {useMemo} from "react";
import {Outlet, useLocation, useNavigate} from "react-router-dom";
import {Image, Layout, Radio} from "antd";
import {CustomRoute, router} from "@/routes.tsx";
import './index.scss'
import {RadioChangeEvent} from "antd/es/radio/interface";

const {Header} = Layout

const HeaderBar: React.FC = () => {
    const items = useMemo(() => {
        const menu_items = router.routes.filter(item => item.path === '/')[0].children as CustomRoute[]
        return menu_items?.filter(i => i?.hidden !== true).map(i => {
            return {label: i.name, value: i.path}
        })
    }, []);

    const location = useLocation()
    const navigate = useNavigate()
    const onClick = (e: RadioChangeEvent) => {
        navigate(e.target.value)
    };

    return (<div>
        <Layout className={'header'}>
            <Header>
                <Image src={'/logo.png'} width={50} height={50} preview={false}/>
                <Radio.Group
                    value={location.pathname}
                    onChange={onClick}
                    className={'menu'}
                >
                    {items.map((label) => (<Radio.Button
                        value={label.value}
                        key={label.value}
                        className={'item'}
                    >
                        {label.label}
                    </Radio.Button>))}
                </Radio.Group>
            </Header>
            <div className={'children'}>
                <Outlet/>
            </div>
        </Layout>
    </div>)
}

export default HeaderBar
