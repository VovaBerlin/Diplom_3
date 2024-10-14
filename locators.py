from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    INPUT_EMAIL = [By.XPATH, '//label[text()="Email"]/following-sibling::input']
    BUTTON_RESET = [By.XPATH, '//button[text()="Восстановить"]']
    ICON_IN_FIELD_PASSWORD = [By.XPATH, "//*[contains(@class, 'input__icon')]"]
    INPUT_ACTIVE = [By.CSS_SELECTOR, '.input.input_status_active']


class LoginLocators:
    FORGOT_PASSWORD = [By.XPATH, '//a[contains(@href, "/forgot-password")]']
    EMAIL = [By.NAME, "name"]
    PASSWORD = [By.NAME, "Пароль"]
    BUTTON_JOIN = [By.XPATH, "//*[text()='Войти']"]


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = [By.XPATH, '//p[text()="Личный Кабинет"]']
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text()="Конструктор"]/parent::a'
    FEED_BUTTON = By.XPATH, '//p[text()="Лента Заказов"]/parent::a'
    BUN_INGREDIENT = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')
    INGREDIENT_DETAILS = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    EXIT_BUTTON = By.XPATH, '//button[contains(@class,"close")]'
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')
    ORDER_BASKET = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]"
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    ORDER_IDENTIFIER = (By.XPATH, '//p[text()="идентификатор заказа"]')
    WAIT_WINDOW = By.XPATH, "//*[@alt='loading animation']/parent::div"


class UserProfilLocators:
    ORDER_HISTORY_BUTTON = [By.LINK_TEXT, 'История заказов']
    LOGOUT_BUTTON = [By.XPATH, ".//button[text()='Выход']"]


class OrderPageLocators:
    ORDER = [By.XPATH, '//*[contains(@class, "OrderHistory_link")]']
    ORDER_STRUCTURE = By.XPATH, '//p[text()="Cостав"]'
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    CLOSE_MODAL_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]")
    ORDERS_AT_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, "
                                   "'text_type_digits-default')]")
    ORDERS_AT_FEED = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                                "text_type_digits-default']")
    TOTAL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DAILY_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    NUMBER_ORDER_PROGRESS = (By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li')
